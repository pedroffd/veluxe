# Stage 1: Build
FROM node:20-alpine as build-stage
WORKDIR /app
COPY package*.json yarn.lock ./
# Install dependencies (using yarn as lockfile exists)
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build

# Stage 2: Serve
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
