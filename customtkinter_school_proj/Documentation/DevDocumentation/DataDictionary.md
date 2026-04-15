# Data Dictionary

This file defines the structure of each database table used in the program, along with example data.
>[!NOTE]
Did use AI to help build this file as it can create the tables in a far faster and in a better looking fashion than i can

# staff_credentials

Stored in `databases/staff_credentials`. Holds login credentials for staff members.

| Field    | Data Type | Description                        |
|----------|-----------|------------------------------------|
| username | TEXT      | The staff member's login username   |
| password | TEXT      | The staff member's login password   |

# Example Data

| username | password |
|----------|----------|
| Staff    | 123      |



# bookings

Stored in `databases/bookings`. Holds all customer booking records.

| Field            | Data Type | Description                                              |
|------------------|-----------|----------------------------------------------------------|
| name             | TEXT      | Full name of the customer                                |
| customer_type    | TEXT      | Type of customer (reg, gov, staff)                       |
| phone            | TEXT      | Customer's phone number                                  |
| performance_date | TEXT      | The night booked (1, 2 or 3)                             |
| seats_booked     | TEXT      | Comma-separated list of seat IDs (e.g. "A1,A2,A3")       |
| price_paid       | TEXT      | Total price paid in GBP after any discounts              |

# Example Data

| name         | customer_type | phone       | performance_date | seats_booked  | price_paid |
|--------------|---------------|-------------|------------------|---------------|------------|
| John Smith   | reg           | 07412345678 | 1                | A1,A2,A3      | 30         |
| Jane Doe     | gov           | 07498765432 | 2                | B5,B6         | 15         |
| Bob Wilson   | staff         | 07456781234 | 3                | C10           | 5          |
| admin        | admin         | admin       | 1                | D4,D5         | 0          |
