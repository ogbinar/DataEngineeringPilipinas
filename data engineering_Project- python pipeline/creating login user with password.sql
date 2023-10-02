Use AdventureWorksDW2022

-- Creates the login Abousername lrousHazem with password 'yourpassword'.  
CREATE LOGIN cali   
    WITH PASSWORD = 'Atlas123';  
GO  

-- Creates a database user for the login created above.  
CREATE USER cali FOR LOGIN cali;  
GO