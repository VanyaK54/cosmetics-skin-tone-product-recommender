-- Create User Table
CREATE TABLE Users (
    user_id VARCHAR(10) PRIMARY KEY,
    detected_skin_tone VARCHAR(20),
    image_path VARCHAR(255)
);

-- Create Product Table
CREATE TABLE Products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    shade VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2)
);

-- Create Reviews Table
CREATE TABLE Reviews (
    review_id VARCHAR(10) PRIMARY KEY,
    product_id VARCHAR(10),
    user_id VARCHAR(10),
    review_text TEXT,
    sentiment VARCHAR(20),
    polarity_score FLOAT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create Recommendation Output Table
CREATE TABLE ProductRecommendations (
    user_id VARCHAR(10),
    top_positive_product_ids VARCHAR(255),
    top_negative_product_ids VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
