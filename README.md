### **API for a Digital Journal**

#### **Project Overview**

- An API that allows users to create, manage, and organize their personal journal entries. The API will support basic CRUD operations, authentication, and tagging of entries.

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

## Getting Started

To get a local copy up and running you just need to follow the following steps in your terminal;

```
git clone "url"
```

where "url" (without the quotation marks) is the url to this repository.

For example:

```shell
git clone https://github.com/droffilc1/journal.git
```

Here you're copying the contents of the journal repository on GitHub to your computer.

Change to the repository directory on your computer and run the app (if you are not already there):

```shell
cd journal
```

Activate a virtual environment:

- Windows:

```shell
venv\Scripts\activate
```
- Mac/Linux:
```shell
source venv/bin/activate
```

Install dependencies:

```shell
python3 install -r requirements.txt
```

Run the application:

```shell
python3 manage.py runserver
```

### Steps to Run the Docker Container

[](https://github.com/droffilc1/journal?tab=readme-ov-file#steps-to-run-the-docker-container)

1. **Pull the Docker Image**
    
    Pull the Docker image from DockerHub:
    
    ```shell
    docker pull droffilc1/journal:latest
    ```
    
2. **Run the Docker Container**
    
    Run the container in detached mode, mapping port 8080 on your local machine to port 8080 in the container:
    
    ```shell
    docker run -dp 8080:8080 --name journal droffilc1/journal:latest
    ```
    
3. **Check Running Containers**
    
    Verify that the container is running:
    
    ```shell
    docker ps
    ```
    
    You should see the `journal` container listed.
    
4. **Access the Application**
    
    Open a web browser and navigate to:
    
    ```shell
    http://localhost:8080
    ```
    
    You should see the journal application running.

#### **APIs Endpoints**

1. **User Authentication**

   - **Register:** POST `/api/v1/dj-rest-auth/register/`
   - **Login:** POST `/api/v1/dj-rest-auth/login/`

2. **Journal Entries**

   - **Create Entry:** POST `/api/entries/`
   - **List Entries:** GET `/api/entries/`
   - **Retrieve Entry:** GET `/api/entries/{id}/`
   - **Update Entry:** PUT `/api/entries/{id}/`
   - **Delete Entry:** DELETE `/api/entries/{id}/`

3. **Tags**

   - **List Tags:** GET `/api/tags/`
   - **Filter Entries by Tag:** GET `/api/entries/?tag={tag_name}`

4. **Categories**

   - **List Categories:** GET `/api/categories/`
   - **Assign Category to Entry:** PATCH `/api/entries/{id}/category/`

5. **Search**

   - **Search Entries:** GET `/api/entries/search/?q={query}`
