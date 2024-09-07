### **API for a Digital Journal**

#### **Project Overview**

- **Purpose:** An API that allows users to create, manage, and organize their personal journal entries. The API will support basic CRUD operations, authentication, and tagging of entries.

#### **Core Features**

1. **User Authentication**

   - **Registration:** Users can create an account to access the journal.
   - **Login:** Users log in to manage their entries.
   - **Token Authentication:** Secure the API with token-based authentication.

2. **Journal Entries**

   - **Create Entry:** Users can create new journal entries, including a title, content, and tags.
   - **Read Entries:** Users can retrieve a list of their entries, or view a specific entry.
   - **Update Entry:** Users can update existing entries.
   - **Delete Entry:** Users can delete entries they no longer need.

3. **Tagging System**

   - **Tag Entries:** Users can tag their entries with relevant keywords.
   - **Filter by Tags:** Users can filter their entries based on tags.

4. **Search Functionality**

   - **Search Entries:** Implement a search feature that allows users to find entries by keywords in the title or content.

5. **Drafts and Publishing**

   - **Draft Mode:** Users can save entries as drafts before publishing.
   - **Publish Entry:** Users can publish a draft entry, making it visible in the main list.

6. **Journal Categories**

   - **Create Categories:** Users can categorize their journal entries (e.g., Work, Personal, Ideas).
   - **Assign Entries to Categories:** Users can assign entries to specific categories for better organization.

#### **APIs to Implement**

1. **User Authentication**

   - **Register:** POST `/api/v1/dj-rest-auth/register/`
   - **Login:** POST `/api/v1/dj-rest-auth/login/`

2. **Journal Entries**

   - **Create Entry:** POST `/api/v1/entries/`
   - **List Entries:** GET `/api/v1/entries/`
   - **Retrieve Entry:** GET `/api/v1/entries/{id}/`
   - **Update Entry:** PUT `/api/v1/entries/{id}/`
   - **Delete Entry:** DELETE `/api/v1/entries/{id}/`

3. **Tags**

   - **List Tags:** GET `/api/v1/tags/`
   - **Filter Entries by Tag:** GET `/api/v1/entries/?tag={tag_name}`

4. **Categories**

   - **List Categories:** GET `/api/v1/categories/`
   - **Assign Category to Entry:** PATCH `/api/v1/entries/{id}/category/`

5. **Search**

   - **Search Entries:** GET `/api/v1/entries/search/?q={query}`
