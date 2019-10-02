FROM ruby:alpine

ENV PORT=8080

EXPOSE ${PORT}

WORKDIR /user/share/memes

RUN apk add --update build-base
RUN gem install sinatra sinatra-contrib thin

COPY server.rb ./

CMD ruby server.rb