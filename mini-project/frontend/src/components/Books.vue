<template>
    <div class="container d-flex justify-content-center align-items-center" style="height: 100vh;">
      <div class="card text-center" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Book Title</h5>
          <h6 class="card-subtitle mb-2 text-muted">Author Name</h6>
          <p class="card-text">ISBN: 123-456-789</p>
        </div>
      </div>
    </div>
  </template>
  <script>
import axios from 'axios';

export default {
  name: 'Books',
  data() {
    return {
      books: []
    };
  },
  created() {
    axios.get('http://localhost:8000/api/books/')
      .then(response => {
        this.books = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>
  