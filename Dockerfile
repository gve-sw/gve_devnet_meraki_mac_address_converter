FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
RUN pip install --upgrade pip
WORKDIR /usr/src/app

COPY . .
