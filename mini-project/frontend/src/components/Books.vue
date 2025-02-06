<template>
  <div class="container d-flex justify-content-center align-items-center" style="height: 100vh;">
    <div v-for="book in books" :key="book.id" class="card text-center" style="width: 18rem; margin: 10px;">
      <div class="card-body">
        <h5 class="card-title">{{ book.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">{{ book.author }}</h6>
        <p class="card-text">Published Date: {{ book.published_date }}</p>
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
    axios.get('http://127.0.0.1:8000//api/books/')
      .then(response => {
        this.books = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>
  