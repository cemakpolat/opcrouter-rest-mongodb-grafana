// init-mongo.js

// Connect to the database
db = db.getSiblingDB('test');  // Switch to the 'test' database

// Create the 'test' collection
db.createCollection('test');

// Insert a sample document into the 'test' collection (optional)
db.test.insert({ name: "Sample Document", createdAt: new Date() });

// You can add more initialization logic here if needed

