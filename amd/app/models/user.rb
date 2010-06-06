require 'digest/sha2'

class User < CassandraObject::Base
  attr_accessor :password

  # The following are the actual columns in the cf
  attribute :name,            :type=>:string
  attribute :first_name,      :type=>:string
  attribute :last_name,       :type=>:string
  attribute :hashed_password, :type=>:string
  attribute :salt,            :type=>:string
  attribute :date_of_birth,   :type=>:date
  attribute :signed_up_at,    :type=>:time_with_zone
  attribute :email,           :type=>:string
  attribute :badge_id,        :type=>:string

  # TODO: if the key is changed to a UUID, this should change to match.
  key :natural, :attributes=>:name

  # TODO: does this work at all?
  association :locationhistorys, :unique=>false, :inverse_of=>:user

  validates_length_of :name, :within => 3..40
  validates_length_of :password, :within => 5..40
  validates_presence_of :name, :email, :password, :password_confirmation, :salt

#TODO: need to manually do this
#  validates_uniqueness_of :name, :email

  validates_confirmation_of :password
  validates_format_of :email, :with => /^([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})$/i, :message => "Invalid email"  

  #TODO: extend this for UUID?
  #TODO: do this manually.
  #attr_protected :salt

  def badge_setup_completed?
    if self.badge_id.nil? || self.badge_id.empty?
      false
    else
      true
    end
  end

  def self.authenticate(login, pass)
    u=get(login)
    return nil if u.nil?
    return u if User.encrypt(pass, u.salt)==u.hashed_password
    nil
  end

  def send_new_password
    new_pass = User.random_string(10)
    self.password = self.password_confirmation = new_pass
    self.save
    Notifications.deliver_forgot_password(self.email, self.login, new_pass)
  end

  def password=(pass)
    @password=pass
    self.salt = User.random_string(10)
    self.hashed_password = User.encrypt(@password, self.salt)
  end

  def self.encrypt(pass, salt)
    Digest::SHA2.hexdigest(pass+salt)
  end

  def self.random_string(len)
    chars = ("a".."z").to_a + ("A".."Z").to_a + ("0".."9").to_a
    newpass = ""
    1.upto(len) do |i|
      newpass << chars[rand(chars.size-1)]
    end
    return newpass
  end
end
