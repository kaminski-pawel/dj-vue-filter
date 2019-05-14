<template>
  <div class="hello">
  <main role="main" class="container">

    <h3>Filter Journals</h3>
    <form method="GET" action=".">
      <div class="form-row">
          <div class="form-group col-12">
              <div class="input-group">
                  <input class="form-control py-2 border-right-0 border" type="search" name="title_contains" placeholder="Title contains..." />
                  <span class="input-group-append">
                      <div class="input-group-text bg-transparent">
                          <i class="fa fa-search"></i>
                      </div>
                  </span>
              </div>
          </div>
      </div>
      <div class="form-row">
          <div class="form-group col-12">
              <div class="input-group">
                  <input class="form-control py-2 border-right-0 border" type="search" name="id_exact" placeholder="ID exact..." />
                  <span class="input-group-append">
                      <div class="input-group-text bg-transparent">
                          <i class="fa fa-search"></i>
                      </div>
                  </span>
              </div>
          </div>
      </div>
      <div class="form-row">
          <div class="form-group col-12">
              <div class="input-group">
                  <input class="form-control py-2 border-right-0 border" type="search" name="title_or_author" placeholder="Title or author..." />
                  <span class="input-group-append">
                      <div class="input-group-text bg-transparent">
                          <i class="fa fa-search"></i>
                      </div>
                  </span>
              </div>
          </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-2 col-lg-2">
          <label for="viewCountMin">Minimum View Count</label>
          <input type="number" min=0 class="form-control" id="viewCountMin" placeholder="0" name="view_count_min">
        </div>
        <div class="form-group col-md-2 col-lg-2">
          <label for="viewCountMax">Maximum View Count</label>
          <input type="number" min=0 class="form-control" id="viewCountMax" placeholder="10000?" name="view_count_max">
        </div>
        <div class="form-group col-md-2 col-lg-2">
          <label for="publishDateMin">Publish date minimum</label>
          <input type="date" class="form-control" id="publishDateMin" name="date_min">
        </div>
        <div class="form-group col-md-2 col-lg-2">
          <label for="publishDateMax">Publish date maximum</label>
          <input type="date" class="form-control" id="publishDateMax" name="date_max">
        </div>
        <div class="form-group col-md-4">
          <label for="category">Category</label>
          <select id="category" class="form-control" name="category">
            <option selected>Choose...</option>
            <option v-for="cat in categories" value="cat">{{ cat }}</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="reviewed" name="reviewed">
          <label class="form-check-label" for="reviewed">
            Reviewed
          </label>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="notReviewed" name="notReviewed">
          <label class="form-check-label" for="notReviewed">
            Not reviewed
          </label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Search</button>
    </form>

    <hr>
    <div class="row">
      <div class="spinner-border" role="status" v-if="loading">
        <span class="sr-only">Loading...</span>
      </div>
      <ul>
          <li v-for="journal in queryset">
            {{ journal.title }}
            <span>Author: {{ journal.author.name }}</span>
            <span v-for="cat in journal.categories">
                {{ cat }}
            </span>
            <span>Publish date: {{ journal.publish_date | formatDate }} </span>
            <span>View count: {{ journal.views }} </span>
            <span>Reviewed: {{ journal.reviewed }}</span>
          </li>
          <hr>
      </ul>
    </div>

  </main>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'DynForm',
  data(){
    return {
      categories: ['Sport', 'Lifestyle', 'Music', 'Coding', 'Travelling'],
      queryset: [],
      loading: false,
      state: {
        results: [],
        loading: false,
        error: null
      }
    }
  },
  filters: {
    formatDate(value){
      return value.split('T')[0]
    }
  },
  mounted(){
    this.loading = true
    axios.get('http://127.0.0.1:8000/api/')
      .then(response => {
        this.loading = false
        this.queryset = response.data
      })
      .catch(error => console.log(error))
  }
}
</script>

<style scoped>
body {
  margin-top: 5rem;
}

ul {
  list-style-type: none;
}
</style>
