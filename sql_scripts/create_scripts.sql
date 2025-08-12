-- ACCOUNTS table
CREATE TABLE accounts (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    plan VARCHAR(255),
    source VARCHAR(255),
    seats INTEGER,
    created_at TIMESTAMP,
    trial_ends_at TIMESTAMP,
    canceled_at TIMESTAMP,
    trial_converted BOOLEAN,
    active_subscription BOOLEAN,
    legacy_plan BOOLEAN,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    country CHAR(2)
);

-- AFFILIATE table
CREATE TABLE affiliate (
    affiliate_number INTEGER PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(20)
);

-- PEOPLE table
CREATE TABLE people (
    id BIGSERIAL PRIMARY KEY,
    address VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    name VARCHAR(255),
    city VARCHAR(255),
    longitude DOUBLE PRECISION,
    state CHAR(2),
    source VARCHAR(255),
    birth_date DATE,
    zip CHAR(5),
    latitude DOUBLE PRECISION,
    created_at TIMESTAMP,
    referral_number INTEGER
);

-- PRODUCTS table
CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY,
    ean CHAR(13),
    title VARCHAR(255),
    category VARCHAR(255),
    vendor VARCHAR(255),
    price DOUBLE PRECISION,
    rating DOUBLE PRECISION,
    created_at TIMESTAMP
);

-- ANALYTIC_EVENTS table
CREATE TABLE analytic_events (
    id BIGINT PRIMARY KEY,
    account_id BIGINT REFERENCES accounts(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    event VARCHAR(255),
    timestamp TIMESTAMP,
    page_url VARCHAR(255),
    button_label VARCHAR(255)
);

-- FEEDBACK table
CREATE TABLE feedback (
    id BIGINT PRIMARY KEY,
    account_id BIGINT REFERENCES accounts(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    email VARCHAR(255),
    date_received TIMESTAMP,
    rating SMALLINT,
    rating_mapped VARCHAR(255),
    body TEXT
);

-- INVOICES table
CREATE TABLE invoices (
    id BIGINT PRIMARY KEY,
    account_id BIGINT REFERENCES accounts(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    payment DOUBLE PRECISION,
    expected_invoice BOOLEAN,
    plan VARCHAR(255),
    date_received TIMESTAMP
);

-- ORDERS table
CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES people(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    product_id INTEGER REFERENCES products(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    subtotal DOUBLE PRECISION,
    tax DOUBLE PRECISION,
    total DOUBLE PRECISION,
    discount DOUBLE PRECISION,
    created_at TIMESTAMP,
    quantity INTEGER
);

-- REVIEWS table
CREATE TABLE reviews (
    id BIGSERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    reviewer VARCHAR(255),
    rating SMALLINT,
    body TEXT,
    created_at TIMESTAMP
);
