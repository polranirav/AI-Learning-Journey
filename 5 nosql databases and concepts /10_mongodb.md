# 📘 MongoDB Beginner Notes (Markdown Conversion)

This document captures MongoDB fundamentals from your PDF, renumbered for your notes.

---

## 1. 🚪 Accessing MongoDB Shell

To start working with MongoDB, open your terminal and type:

```bash
mongo
```

You'll enter the MongoDB shell:

```text
>
```

This is where you can start writing MongoDB commands.

---

## 2. 🏗️ Creating a Database

MongoDB uses the `use` command to switch to a database:

```js
use mydatabase
```

If `mydatabase` does not exist, it will be **created automatically** when you insert data.

---

## 3. 📦 Creating a Collection

Collections are like SQL tables. You can create a collection using:

```js
db.createCollection("users")
```

✅ MongoDB will also **create the collection automatically** if you insert data directly.

---

## 4. ✍️ Inserting One Document

A document is similar to a row in SQL, but in **JSON format**:

```js
db.users.insertOne({ name: "Alice", age: 25 })
```

> This creates the `users` collection (if it doesn’t exist) and inserts one document.

---

## 5. 📥 Inserting Many Documents

To insert multiple entries in one go:

```js
db.users.insertMany([
  { name: "Bob", age: 30 },
  { name: "Carol", age: 22 },
  { name: "Dave", age: 28 }
])
```

> Efficient when populating a new database or bulk uploading.

---

## 6. 🔍 Finding Documents

To display all documents in a collection:

```js
db.users.find()
```

This returns all records in the `users` collection.

---

## 7. 🧾 Making Output Readable with `.pretty()`

Use `.pretty()` to display results in a clean, readable format:

```js
db.users.find().pretty()
```

Example output:
```json
{
  "_id": ObjectId("..."),
  "name": "Alice",
  "age": 25
}
```

---

## 8. 🎯 Finding Documents with Conditions

To find documents matching a condition:

```js
db.users.find({ age: 25 })
```

This will return all users whose age is exactly 25.

---

## 9. 🧠 Displaying Selected Fields (Projection)

To return only specific fields:

```js
db.users.find({}, { name: 1 })
```

This shows only the `name` field of each document (plus `_id` by default).

To exclude `_id`:

```js
db.users.find({}, { name: 1, _id: 0 })
```

---

## 10. 🔍 Using Comparison Operators

| Operator | Meaning         | Example                                |
|----------|------------------|----------------------------------------|
| `$gt`    | Greater than     | `{ age: { $gt: 25 } }`                |
| `$lt`    | Less than        | `{ age: { $lt: 30 } }`                |
| `$gte`   | Greater or equal | `{ age: { $gte: 18 } }`               |
| `$lte`   | Less or equal    | `{ age: { $lte: 40 } }`               |
| `$ne`    | Not equal        | `{ age: { $ne: 22 } }`                |
| `$in`    | In list          | `{ age: { $in: [22, 25, 30] } }`      |
| `$nin`   | Not in list      | `{ age: { $nin: [22, 25, 30] } }`     |

Example usage:

```js
db.users.find({ age: { $gt: 25 } })
```
---

## 11. 🧠 Logical Operators: AND, OR

### 🔸 `$and` Operator

```js
db.users.find({
  $and: [{ age: { $gt: 20 } }, { age: { $lt: 30 } }]
})
```

This returns users whose age is greater than 20 **and** less than 30.

---

### 🔹 `$or` Operator

```js
db.users.find({
  $or: [{ name: "Alice" }, { name: "Bob" }]
})
```

This returns users whose name is either Alice **or** Bob.

---

## 12. 🔢 Counting Documents

To count how many documents are in a collection:

```js
db.users.count()
```

To count documents that match a condition:

```js
db.users.find({ age: 25 }).count()
```

✅ Tip: For newer versions, `countDocuments()` is preferred:
```js
db.users.countDocuments({ age: 25 })
```

---

## 13. 🔃 Sorting Results

Use `.sort()` to sort documents by a field:

```js
db.users.find().sort({ age: 1 })   // Ascending
db.users.find().sort({ age: -1 })  // Descending
```

Sort by any field, like `name`, `created_at`, etc.

---

## 14. 🎛️ Limiting Results

Use `.limit(n)` to restrict the number of documents returned:

```js
db.users.find().limit(5)
```

Shows only the **first 5** documents.

---

## 15. ⏭️ Skipping Results

Use `.skip(n)` to skip over the first n documents:

```js
db.users.find().skip(5)
```

Useful for **pagination** when combined with `.limit()`:

```js
db.users.find().skip(5).limit(5)
```
---

## 16. ✏️ Updating One Document

To update the first matching document:

```js
db.users.updateOne(
  { name: "Alice" },
  { $set: { age: 27 } }
)
```

- Finds user named Alice
- Updates her age to 27

---

## 17. 🔁 Updating Many Documents

To update **all** matching documents:

```js
db.users.updateMany(
  { age: { $lt: 18 } },
  { $set: { status: "minor" } }
)
```

This adds a new field `status` to all users under 18.

---

## 18. 🔧 Other Update Operators

| Operator | Description                        | Example Use                          |
|----------|------------------------------------|--------------------------------------|
| `$set`   | Sets a new value                   | `{ $set: { field: value } }`        |
| `$unset` | Removes a field from the document  | `{ $unset: { field: "" } }`         |
| `$inc`   | Increments a number                | `{ $inc: { age: 1 } }`              |
| `$rename`| Renames a field                    | `{ $rename: { "old": "new" } }`     |

Example:

```js
db.users.updateOne(
  { name: "Bob" },
  { $inc: { age: 1 } }
)
```

This increases Bob's age by 1.

---

## 19. 🗑️ Deleting One Document

```js
db.users.deleteOne({ name: "Carol" })
```

Removes the **first** matching document.

---

## 20. 🧹 Deleting Many Documents

```js
db.users.deleteMany({ age: { $lt: 18 } })
```

Deletes all users under 18.

---

## 21. 🗃️ Dropping a Collection

To completely remove a collection:

```js
db.users.drop()
```

- Deletes all documents **and** the structure.
- No undo — use with caution!

---

## 22. 🧨 Dropping a Database

To delete the entire database:

```js
use mydatabase
db.dropDatabase()
```

- Must switch to the database first using `use`
- Then run `dropDatabase()`

---

## 23. 🧩 Creating Indexes

Indexes improve query speed for specific fields.

```js
db.users.createIndex({ name: 1 })   // Ascending index on 'name'
```

To create descending index:

```js
db.users.createIndex({ age: -1 })
```

You can view existing indexes with:

```js
db.users.getIndexes()
```

---

## 24. 🆔 Understanding ObjectId and `_id`

Every document has a unique `_id` field, often an **ObjectId**:

```json
"_id": ObjectId("64c99a4d827f497aaf127f18")
```

You can create or search by it:

```js
db.users.find({ _id: ObjectId("64c99a4d827f497aaf127f18") })
```

> If you don’t manually add `_id`, MongoDB will create one for you.

---

## 25. 🖥️ Using MongoDB Compass (GUI)

MongoDB Compass is a visual tool for managing MongoDB.

With Compass, you can:
- View collections and databases
- Insert, edit, delete data
- Run queries without shell
- Analyze schema and indexes

✅ It's useful if you prefer working with a UI instead of the terminal.

---

## 26. 📊 Introduction to Aggregation

Aggregation is used to **analyze and transform data** in MongoDB.

It’s like SQL’s `GROUP BY`, `SUM()`, `AVG()`…

Aggregation uses a **pipeline of stages** (like `match`, `group`, `project`).

---

## 27. 🧮 Aggregation Example: Group and Count

Let’s count how many users exist per age group:

```js
db.users.aggregate([
  { $group: { _id: "$age", count: { $sum: 1 } } }
])
```

This returns:
```json
{ "_id": 25, "count": 2 }
{ "_id": 30, "count": 1 }
```

✅ `_id` here is the field you’re grouping by (`age`)

---

## 28. 🎯 Aggregation with `$match` and `$avg`

Filter + calculate average age:

```js
db.users.aggregate([
  { $match: { gender: "female" } },
  { $group: { _id: "$gender", avgAge: { $avg: "$age" } } }
])
```

💡 You can chain multiple stages in the aggregation pipeline:
- `$match`: filters like `WHERE`
- `$group`: works like `GROUP BY`
- `$sum`, `$avg`, `$min`, `$max`: do calculations

---
## 31. 🎯 `$match`, `$project`, and `$set`

### `$match`: Filters documents (like SQL WHERE)

```js
{ $match: { age: { $gt: 18 } } }
```

### `$project`: Shapes the output

```js
{ $project: { name: 1, age: 1, _id: 0 } }
```

### `$set`: Adds or modifies fields

```js
{ $set: { status: "active" } }
```

You can combine them:

```js
db.users.aggregate([
  { $match: { age: { $gt: 25 } } },
  { $set: { adult: true } },
  { $project: { name: 1, age: 1, adult: 1, _id: 0 } }
])
```

---

## 32. 🔤 String Operators in MongoDB

| Operator     | Description                            | Example                                             |
|--------------|----------------------------------------|-----------------------------------------------------|
| `$concat`    | Concatenates strings                   | `{ fullName: { $concat: ["$first", " ", "$last"] } }` |
| `$toUpper`   | Converts to uppercase                  | `{ upper: { $toUpper: "$name" } }`                  |
| `$toLower`   | Converts to lowercase                  | `{ lower: { $toLower: "$name" } }`                  |
| `$substr`    | Substring from string                  | `{ part: { $substr: ["$name", 0, 3] } }`            |
| `$trim`      | Trims whitespace or chars              | `{ clean: { $trim: { input: "$name" } } }`          |
| `$regexMatch`| Checks pattern match                   | `{ match: { $regexMatch: { input: "$email", regex: "@gmail.com$" } } }` |

---

## 33. ➕ Arithmetic Operators

| Operator     | Description                            | Example                                        |
|--------------|----------------------------------------|------------------------------------------------|
| `$add`       | Adds numbers                           | `{ total: { $add: ["$score1", "$score2"] } }` |
| `$subtract`  | Subtracts values                       | `{ diff: { $subtract: ["$max", "$min"] } }`   |
| `$multiply`  | Multiplies numbers                     | `{ product: { $multiply: [2, "$price"] } }`   |
| `$divide`    | Divides values                         | `{ ratio: { $divide: ["$value", "$total"] } }`|
| `$round`     | Rounds to nearest int/decimal          | `{ rounded: { $round: ["$value", 2] } }`      |
| `$abs`       | Absolute value                         | `{ absVal: { $abs: "$score" } }`              |

---

## 34. ⚙️ Conditional Operators

| Operator   | Description                                  | Example |
|------------|----------------------------------------------|---------|
| `$cond`    | If-then-else logic                           | `{ result: { $cond: [ { $gte: ["$marks", 50] }, "Pass", "Fail" ] } }` |
| `$ifNull`  | Replaces null with default                   | `{ value: { $ifNull: ["$address", "N/A"] } }` |
| `$switch`  | Multiple if-else ladder                      | 
```js
{
  result: {
    $switch: {
      branches: [
        { case: { $eq: ["$grade", "A"] }, then: "Excellent" },
        { case: { $eq: ["$grade", "B"] }, then: "Good" }
      ],
      default: "Average"
    }
  }
}
```

---
## 35. 🧠 Example: Combining All Operators

```js
db.users.aggregate([
  { $match: { status: "active" } },
  { $set: {
      fullName: { $concat: ["$first", " ", "$last"] },
      isAdult: { $cond: [ { $gte: ["$age", 18] }, true, false ] },
      ageIn5Years: { $add: ["$age", 5] }
    }
  },
  { $project: { fullName: 1, isAdult: 1, ageIn5Years: 1, _id: 0 } }
])
```

✅ This example filters users, builds new fields, and formats the output — all in one pipeline!

---
---

## 36. 📆 Date and Time Operators

Used to extract or format dates from fields like `createdAt`, `dob`, etc.

| Operator         | Description                            | Example |
|------------------|----------------------------------------|---------|
| `$dateToString`  | Formats a date to a string             | `{ $dateToString: { format: "%Y-%m-%d", date: "$dob" } }` |
| `$year`          | Extracts year                          | `{ $year: "$createdAt" }` |
| `$month`         | Extracts month                         | `{ $month: "$createdAt" }` |
| `$dayOfWeek`     | Gets weekday (1 = Sunday)              | `{ $dayOfWeek: "$createdAt" }` |

✅ Example: Add birth year to each document:

```js
db.users.aggregate([
  { $project: {
      name: 1,
      birthYear: { $year: "$dob" }
  }}
])
```

---

## 37. 🧠 System and User Variables

MongoDB allows access to built-in variables with `$$` syntax.

| Variable      | Description                             |
|---------------|-----------------------------------------|
| `$$NOW`       | Current date/time                       |
| `$$ROOT`      | Refers to root document                 |
| `$$CURRENT`   | Refers to current document inside stage |
| `$$REMOVE`    | Removes field inside `$set`             |

✅ Example:

```js
db.users.aggregate([
  { $project: {
      now: "$$NOW",
      all: "$$ROOT",
      current: "$$CURRENT"
  }}
])
```

---

## 38. 🔗 `$lookup`: JOIN Like SQL

Join two collections: `orders` and `users`

```js
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }
  }
])
```

- `from`: collection to join (`users`)
- `localField`: in `orders`
- `foreignField`: in `users`
- `as`: result field to hold joined data

---

## 39. 🛡️ Schema Validation

MongoDB allows validating structure at collection level using `$jsonSchema`.

```js
db.createCollection("products", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "price"],
      properties: {
        name: { bsonType: "string" },
        price: { bsonType: "double", minimum: 0 }
      }
    }
  }
})
```

- Validates every insert/update
- Similar to defining schema in SQL or Mongoose

---

## 40. 🗂️ Indexing in MongoDB

Improve query performance by indexing frequently searched fields.

### Create a single-field index:

```js
db.users.createIndex({ name: 1 }) // ascending
```

### Compound index (multiple fields):

```js
db.users.createIndex({ name: 1, age: -1 })
```

### View all indexes:

```js
db.users.getIndexes()
```

> MongoDB uses B-Trees under the hood. Index wisely — avoid over-indexing.

---
