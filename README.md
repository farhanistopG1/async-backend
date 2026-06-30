## Production Deployment

Customer Support Engine V2 is deployed as a production service on a Linux VPS using FastAPI, PostgreSQL, pgvector, systemd, nginx, and HTTPS.

### Production Stack

* FastAPI
* PostgreSQL
* pgvector
* LangChain Recursive Character Text Splitter
* Semantic Search
* Linux VPS
* systemd
* nginx Reverse Proxy
* HTTPS (Let's Encrypt)

### Production Pipeline

Knowledge Files

↓

Recursive Chunking

↓

Embedding Generation

↓

PostgreSQL + pgvector

↓

Semantic Retrieval

↓

LLM Response Generation

### Deployment Challenges Solved

During production deployment, the following issues were resolved:

* Runtime dependency management
* PostgreSQL authentication
* pgvector installation and activation
* Database role permissions
* Schema initialization
* Knowledge bootstrapping
* Production startup debugging using journalctl

### Key Engineering Lesson

A production deployment is more than deploying application code.

The complete system requires:

* Runtime dependencies
* Database connectivity
* Extensions
* Permissions
* Schema creation
* Knowledge seeding
* Health verification

Only after every layer is operational can the application begin serving requests successfully.
