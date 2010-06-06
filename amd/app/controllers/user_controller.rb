class UserController < ApplicationController
  before_filter :login_required, :only=>['setup_badge', 'change_password', 'hidden']

  def signup
    if request.post?
      @user = User.new :name=>              @params[:name], \
                   :password=>              @params[:password], \
                   :password_confirmation=> @params[:password_confirmation], \
                   :email=>                 @params[:email]
      if @user.save
        session[:user] = User.authenticate(@user.name, @user.password)
        flash[:message] = "Signup successful"
        redirect_to :action => "setup_badge"          
      else
        flash[:warning] = "Signup unsuccessful. Maybe the database is dead?"
      end
    end
  end

  def login
    if request.post?
      if session[:user] = User.authenticate(params[:user][:login], params[:user][:password])
        flash[:message]  = "Login successful"
        redirect_to_stored
      else
        flash[:warning] = "Login unsuccessful"
      end
    end
  end

  def logout
    session[:user] = nil
    flash[:message] = 'Logged out'
    redirect_to :action => 'login'
  end

  def forgot_password
    if request.post?
      u= User.get(params[:user])
      if u and u.send_new_password
        flash[:message]  = "A new password has been sent by email."
        redirect_to :action=>'login'
      else
        flash[:warning]  = "Couldn't send password"
      end
    end
  end

  def change_password
    @user=session[:user]
    if request.post?
      @user.update_attributes(:password=>params[:user][:password], :password_confirmation => params[:user][:password_confirmation])
      if @user.save
        flash[:message]="Password Changed"
      end
    end
  end

  def profile
    @user=session[:user]

    unless @user.badge_setup_completed?
      redirect_to :action=>'setup_badge'
    end
  end

  def setup_badge
    @user=session[:user]
    if request.post?
      @user.update_attributes(:badge_id=>params[:badge_id])
      if @user.save
        flash[:message]='Underneath the spreading chestnut tree, I sold you and you sold me.'
      end
    end
  end

  def hidden
  end
end
