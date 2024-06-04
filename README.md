## Scraping Site link
https://interwood.pk/collections/beds/products/woodson-bed-brown-single

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```bash
# Example for Python Flask Backend
python -m pip install -r requirements.txt

# Example for React Frontend
npm install
```

### Installing

A step by step series of examples that tell you how to get a development environment running.

#### Setting up the Backend

Navigate to the backend directory:

```bash
cd backend
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python app.py
```

## Database
Mysql

DB_Name = scraping
User = root
Password = 
Host = localhost

#### Setting up the Frontend

Navigate to the frontend directory:

```bash
cd frontend
```

Install the necessary node modules:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

The server should now be running at [http://localhost:3000](http://localhost:3000).

## Usage

How to use the application, including any available endpoints and their expected parameters.

### Backend

- **/scrape** POST: Endpoint to scrape data from a provided URL. Expects a JSON payload with the URL.
  ```json
  {
    "url": "https://example.com/product"
  }
  ```

### Frontend

Interact with the React application through the web interface at [http://localhost:3000](http://localhost:3000).

## Running the tests

Explain how to run the automated tests for this system.

```bash
# For backend
pytest

# For frontend
npm test
```

## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used for the backend
* [React](https://reactjs.org/) - The web framework used for the frontend
* [Bootstrap](https://getbootstrap.com/) - Used for styling the frontend

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
