require 'sinatra'
require 'sinatra/json'

set :port, ENV['PORT'] || 9292 
set :bind, ENV['HOST'] || '0.0.0.0'

get '/' do
  json msg: 'It works!'
end
