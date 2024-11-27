require 'swagger_helper'

RSpec.describe 'api/app_users', type: :request do

  path '/app_users' do
    get('Retrieves a list of app users') do
      response 200, 'Current app users' do
        schema type: :array, items: { '$ref' => '#/components/schemas/AppUser' }
        run_test!
      end
    end

    post('Creates a new app user') do
      consumes 'application/x-www-form-urlencoded;charset=UTF-8'
      parameter name: :authenticity_token, in: :formData, type: :string, required: true, description: 'CSRF token'
      parameter name: :'app_user[name]', in: :formData, type: :string, required: true, description: 'Name of the app user'
      parameter name: :'app_user[email]', in: :formData, type: :string, required: true, description: 'Email of the app user'
      parameter name: :'app_user[preferences]', in: :formData, type: :string, required: true, description: 'Preferences of the app user'
      parameter name: :commit, in: :formData, type: :string, required: true, description: 'Submit button value'

      response 201, 'App user created' do
        schema '$ref' => '#/components/schemas/AppUser'

        let(:authenticity_token) { 'RbvulqBFVlGQfZzTTxVDD07J6laRVQVdsWMnlZNEC6rUXjg5yiaSn9KhE4zYTnWeHHfddeFpNk0-hGrC4VltIQ' }
        let(:'app_user[name]') { 'Anton' }
        let(:'app_user[email]') { 'aplaksin2000@gmail.com' }
        let(:'app_user[preferences]') { 'I like reading news about eroupean politics and science' }
        let(:commit) { 'Create App user' }

        run_test!
      end
    end
  end

  path '/app_users/{id}' do
    get('Retrieves a specific app user') do
      response 200, 'App user found' do
        schema '$ref' => '#/components/schemas/AppUser'

        let(:id) { AppUser.create(name: 'John Doe', email: 'john@example.com', preferences: 'politics and science').id }
        run_test!
      end

      response 404, 'App user not found' do
        let(:id) { 'nonexistent_id' }
        run_test!
      end
    end

    put('Updates a specific app user') do
      response 200, 'App user updated' do
        schema '$ref' => '#/components/schemas/AppUser'

        let(:id) { AppUser.create(name: 'John Doe', email: 'john@example.com', preferences: 'politics and science').id }
        let(:app_user) { { name: 'Jane Doe', email: 'jane@example.com', preferences: 'culture' } }

        run_test!
      end
    end

    delete('Deletes a specific app user') do
      response 204, 'App user deleted' do
        let(:id) { AppUser.create(name: 'John Doe', email: 'john@example.com', preferences: 'politics and science').id }
        run_test!
      end

      response 404, 'App user not found' do
        let(:id) { 'nonexistent_id' }
        run_test!
      end
    end
  end
end