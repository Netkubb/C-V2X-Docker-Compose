from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://mongo:mongo@mongo:27017")
db = client["cv2x"]

# Define collections
users_collection = db["users"]
drivers_collection = db["drivers"]
cars_collection = db["cars"]
cameras_collection = db["cameras"]
rsus_collection = db["rsus"]

# Insert data into 'drivers' collection
drivers_data = [
    {
        "_id": ObjectId("603d2f8e2e3b1a3e3f5b2a70"),
        "first_name": "John",
        "last_name": "Doe",
        "phone_no": "0123456789",
        "createdAt": datetime.fromisoformat("2023-01-01T00:00:00")
    }
]
drivers_collection.insert_many(drivers_data)

# Insert data into 'cars' collection
cars_data = [
    {
        "_id": ObjectId("5b360fdea392d731829ded18"),
        "name": "Car01",
        "license_plate": "ABC123",
        "model": "XYZ",
        "driver_id": ObjectId("603d2f8e2e3b1a3e3f5b2a70"),
        "createdAt": datetime.fromisoformat("2023-01-01T00:00:00")
    }
]
cars_collection.insert_many(cars_data)

# Insert data into 'cameras' collection
cameras_data = [
    {
        "_id": ObjectId("5b360fdea392d731829ded19"),
        "name": "Front Camera Car01",
        "position": "Front",
        "car_id": ObjectId("5b360fdea392d731829ded18"),
        "createdAt": datetime.fromisoformat("2023-01-01T00:00:00")
    }
]
cameras_collection.insert_many(cameras_data)

# Insert data into 'rsus' collection
rsus_data = [
    {
        "_id": ObjectId("62261a65d66c6be0a63c051f"),
        "name": "RSU01",
        "recommended_speed": "100",
        "latitude": "13.737868",
        "longitude": "100.534457",
        "lane_changing": "0",
        "createdAt": datetime.fromisoformat("2023-01-01T00:00:00")
    }
]
rsus_collection.insert_many(rsus_data)

# Insert data into 'users' collection
users_data = [
    {
        "username": "adminUser",
        "password": "$2a$10$svnJcJDLCC.WaArioXUeoOvo2yF2tVGjViewkQh3Hpa0uxrC75jO2",
        "role": "admin",
        "driver_id": None,
        "resetPasswordToken": None,
        "resetPasswordExpire": None,
        "createdAt": datetime.fromisoformat("2023-01-01T00:00:00")
    },
    {
        "username": "driverUser1",
        "password": "$2a$10$Omnkky4FiF83EL4qqAbSmeoheUiSiC6Bh/YpTDIt2xFAsPjq7E0aG",
        "role": "driver",
        "driver_id": ObjectId("603d2f8e2e3b1a3e3f5b2a70"),
        "resetPasswordToken": None,
        "resetPasswordExpire": None,
        "createdAt": datetime.fromisoformat("2023-01-01T00:00:00")
    }
]
users_collection.insert_many(users_data)

print("Seeding completed.")

# Close the client
client.close()