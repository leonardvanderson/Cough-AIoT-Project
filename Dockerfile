FROM nodered/node-red:latest

# Install your required dashboard and influxdb nodes
RUN npm install @flowfuse/node-red-dashboard@1.32.0 node-red-contrib-influxdb@0.7.0

# Copy your flow file into the container
COPY flows.json /data/flow_files.json
COPY flows_cred.json /data/flows_cred.json
COPY settings.js /data/settings.js

# Tell Node-RED to use this flow file on startup
ENV FLOWS=flow_files.json
