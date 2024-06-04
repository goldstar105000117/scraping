import React from 'react';
import axios from 'axios';

class App extends React.Component {
  state = {
    data: null,
    error: null,
    loading: false
  };

  fetchData = () => {
    this.setState({ loading: true, error: null });
    axios.post('http://localhost:5000/scrape', { url: 'https://interwood.pk/collections/beds/products/woodson-bed-brown-single' })
      .then(response => {
        this.setState({ data: response.data, loading: false, error: null });
      })
      .catch(error => {
        this.setState({ error: error.message, loading: false });
      });
  };

  render() {
    const { data, error, loading } = this.state;
    return (
      <div className="container mt-5">
        <h1 className="mb-3">Hello!</h1>
        <button className="btn btn-primary" onClick={this.fetchData} disabled={loading}>
          {loading ? 'Loading...' : 'Fetch Data'}
        </button>
        {data && (
          <div className="mt-3">
            <h2>Product Details:</h2>
            <p><strong>Title:</strong> {data.title}</p>
            <p><strong>Price:</strong> {data.price}</p>
            <div>
              <strong>Description:</strong>
              <div dangerouslySetInnerHTML={{ __html: data.description }} />
            </div>
          </div>
        )}
        {error && (
          <div className="alert alert-danger mt-3" role="alert">
            Error scraping: {error}
          </div>
        )}
      </div>
    );
  }
}

export default App;
