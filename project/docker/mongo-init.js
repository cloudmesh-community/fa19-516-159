db.createUser(
    {
        user: "azebrows",
        pwd: *****,
        roles: [
            {
                role: "readWrite",
                db: "cloudmesh"
            }
        ]
    }
);
