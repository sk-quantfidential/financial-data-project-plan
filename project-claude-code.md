# Financial Data Project

## Should go into claude init file
Starting from the main branch, create a new feature branch to define our initial protobuf schema.  I want you to create a modern, professional set of ProtoBuf Schemas for a suite of Financial Data applications and components.  All serialised data types, and request and response interactions for the various components will be maintained under the proto directory. Here is my vision:

## Initial Project Protobuf Schema 
APPLICATION OVERVIEW
This application is a modern, resilient, asynchronous financial data platform designed to ingest, process, and serve various types of financial data. It uses Protocol Buffers (ProtoBuf) as the primary schema definition language for inter-service communication and data modeling. The MVP will expose a RESTful API for the frontend, with ProtoBuf schemas serving as the canonical source for both internal and external data formats.
The system is built using Rust for backend services, PostgreSQL for persistence, Kafka for asynchronous messaging, and Next.js for the frontend. ProtoBuf schemas will be used to define all financial data types and will serve as the basis for generating RESTful JSON responses and HTML views.

CORE FEATURES
- Real-time ingestion of market data (L1 and L2)
- Aggregation of candle data for charting
- Storage and retrieval of rate values, index values, and economic indicators
- Metadata tagging and schema evolution support
- REST API exposure based on ProtoBuf schema definitions
- Support for multiple financial instruments and asset classes

TECHNICAL REQUIREMENTS
- All data types must be defined using Protocol Buffers v3 syntax
- Schemas must be modular and versioned for future evolution
- Each schema should include:
- Unique identifiers
- Timestamps (event time and ingestion time)
- Source metadata
- Optional fields for extensibility
- Schemas should be optimized for both serialization efficiency and human readability
- Support for nested types and repeated fields where appropriate
- Compatibility with Rust, PostgreSQL, and Kafka serialization/deserialization

DESIGN REQUIREMENTS
- Use clear, descriptive naming conventions for message types and fields
- Group related data types into logical packages (e.g., market, economic, instrument)
- Include comments in the schema to explain field semantics
- Ensure compatibility with RESTful JSON generation tools (e.g., grpc-gateway)
- Design for extensibility: allow optional fields and reserved tags for future use
- Include enums for standardized values (e.g., market status, instrument type)

SPECIFIC FUNCTIONALITY: ENUMERATED FINANCIAL DATA TYPES
You should minimally generate ProtoBuf schemas for the following financial data types:
1. L1 Market Data (Top-of-Book)
- Bid/ask price and size
- Last traded price
- Market status (open, closed, halted)
2. L2 Market Data (Order Book Depth)
- Multiple levels of bid/ask prices and sizes
- Order timestamps and IDs
- Market participant identifiers (optional)
3. Candle Aggregated Data
- Open, high, low, close prices
- Volume
- Time interval (e.g., 1m, 5m, 1h)
4. Rate Value
- Interest rates (e.g., LIBOR, SOFR)
- FX rates (e.g., USD/EUR)
- Rate source and timestamp
5. Index Value
- Index level (e.g., S&P 500)
- Constituent metadata (optional)
- Calculation timestamp
6. Economic Indicator
- Indicator name (e.g., CPI, GDP)
- Value and revision history
- Release timestamp and source
7. Metadata
- Source system or authority
- Region
- Category
- Report
- Data quality flags
- Ingestion timestamp
- Tags and labels
8. Securities Info
- Instrument ID (ISIN, CUSIP, etc.)
- Name, type (equity, bond, derivative)
- Exchange and currency
- Lifecycle dates (issue, maturity)
9. Additional Financial Data Types
- Corporate Actions: dividends, splits, mergers
- Trade Prints: executed trades with counterparty info
- Settlement Instructions: clearing and settlement metadata
- Risk Metrics: volatility, beta, VaR
- News Sentiment: headline, sentiment score, source

The schema will evolve to include workflow requests and responses that will embed these data types.  Imagine that you were these components and build out a set of request and responses that you would need to support a web application like https://ycharts.com

## JS 
