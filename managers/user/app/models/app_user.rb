class AppUser < ApplicationRecord
  after_update_commit -> { broadcast_replace_to "app_users" }
end
