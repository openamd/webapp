class Location < CassandraObject::Base
  attribute :key,  :type=>:integer
  attribute :x,    :type=>:integer
  attribute :y,    :type=>:integer

  # bi-directional associations with read-repair support.
  association :user, :unique=>true, :inverse_of=>:locationhistory

  key :natural, :attributes=>:key

  # Override table name (default name derived from object const)
  @column_family='LocationHistory'
end
