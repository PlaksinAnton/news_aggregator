require 'swagger_helper'

RSpec.describe 'api/app_users', type: :request do

  path '/app_users' do
    get('Retrieves a list of app users') do
      tags 'UI'
      response 200, 'Depicts current app users' do
        schema type: :array, items: { '$ref' => '#/components/schemas/AppUser' }
        run_test!
      end
    end

    post('Creates a new app user') do
      tags 'UI'
      consumes 'application/x-www-form-urlencoded;charset=UTF-8'
      parameter name: :payload, in: :body, schema: {
        type: :object,
        properties: {
          authenticity_token: { type: :string, description: 'CSRF token', example: 'RbvulqBFVlGQfZzTTxVDD07J6laRVQVdsWMnlZNEC6rUXjg5yiaSn9KhE4zYTnWeHHfddeFpNk0-hGrC4VltIQ' },
          app_user: { '$ref' => '#/components/schemas/AppUser' },
          commit: { type: :string, description: 'Submit button value', example: 'Create App user' }
        },
        required: %w[authenticity_token app_user commit]
      }
      response 302, 'Redirects to the User view' do
        # schema '$ref' => '#/components/schemas/AppUser'

        # let(:authenticity_token) { '' }
        # let(:'app_user[name]') { 'Anton' }
        # let(:'app_user[email]') { 'aplaksin2000@gmail.com' }
        # let(:'app_user[preferences]') { 'I like reading news about eroupean politics and science' }
        # let(:commit) { 'Create App user' }

        run_test!
      end
    end
  end

  path '/app_users/{id}' do
    get('Retrieves a specific app user') do
      tags 'UI'
      response 200, 'Depicts specidied app user' do
        schema '$ref' => '#/components/schemas/AppUser'
        # let(:id) { AppUser.create(name: 'John Doe', email: 'john@example.com', preferences: 'politics and science').id }
        run_test!
      end
    end

    put('Updates a specific app user') do
      tags 'UI'
      consumes 'application/x-www-form-urlencoded;charset=UTF-8'
      parameter name: :payload, in: :body, schema: {
        type: :object,
        properties: {
          authenticity_token: { type: :string, description: 'CSRF token', example: 'RbvulqBFVlGQfZzTTxVDD07J6laRVQVdsWMnlZNEC6rUXjg5yiaSn9KhE4zYTnWeHHfddeFpNk0-hGrC4VltIQ' },
          app_user: { '$ref' => '#/components/schemas/AppUser' },
          commit: { type: :string, description: 'Submit button value', example: 'Create App user' }
        },
        required: %w[authenticity_token app_user commit]
      }
      response 302, 'App user updated' do
        schema '$ref' => '#/components/schemas/AppUser'
        # let(:id) { AppUser.create(name: 'John Doe', email: 'john@example.com', preferences: 'politics and science').id }
        # let(:app_user) { { name: 'Jane Doe', email: 'jane@example.com', preferences: 'culture' } }
        run_test!
      end
    end

    delete('Deletes a specific app user') do
      tags 'UI'
      consumes 'application/x-www-form-urlencoded;charset=UTF-8'
      parameter name: :payload, in: :body, schema: {
        type: :object,
        properties: {
          authenticity_token: { type: :string, description: 'CSRF token', example: 'RbvulqBFVlGQfZzTTxVDD07J6laRVQVdsWMnlZNEC6rUXjg5yiaSn9KhE4zYTnWeHHfddeFpNk0-hGrC4VltIQ' },
        },
        required: %w[authenticity_token app_user commit]
      }
      response 303, 'App user deleted' do
        let(:id) { AppUser.create(name: 'John Doe', email: 'john@example.com', preferences: 'politics and science').id }
        run_test!
      end
    end
  end

  path '/app_users/{id}' do
    post('Make news request to a queue for spesified user') do
      tags 'News logic'
      consumes 'application/x-www-form-urlencoded;charset=UTF-8'
      parameter name: :payload, in: :body, schema: {
        type: :object,
        properties: {
          authenticity_token: { type: :string, description: 'CSRF token', example: 'RbvulqBFVlGQfZzTTxVDD07J6laRVQVdsWMnlZNEC6rUXjg5yiaSn9KhE4zYTnWeHHfddeFpNk0-hGrC4VltIQ' },
        },
        required: %w[authenticity_token app_user commit]
      }
      response 303, 'Redirects to user view' do
        run_test!
      end
    end
  end

  path '/callback' do
    post('Callback for getting realtime updates about news request status') do
      tags 'News logic'
      consumes 'application/json'
      parameter name: :payload, in: :body, schema: {
        type: :object,
        properties: {
          app_user: {
            type: :object,
            properties: {
              use_id: { type: :integer, example: '1' },
              message: { type: :string,  example: 'Message sent! Check your Email.' },
            },
          },
        },
      }

      response 200, 'User view updated' do
        run_test!
      end
    end
  end
end
