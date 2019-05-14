<template>
  <div class="hello">
  <main role="main" class="container">

    <h3>Filter Journals</h3>
    <form method="GET" @submit.prevent="onSubmit" action=".">
      <div class="form-row">
          <div class="form-group col-12">
              <div class="input-group">
                  <input class="form-control py-2 border-right-0 border" type="search"
                  v-model="title_contains" name="title_contains" placeholder="Title contains..." />
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
                  <input class="form-control py-2 border-right-0 border" type="search"
                  v-model="id_exact" name="id_exact" placeholder="ID exact..." />
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
                  <input class="form-control py-2 border-right-0 border" type="search"
                  v-model="title_or_author" name="title_or_author" placeholder="Title or author..." />
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
          <input type="number" min=0 class="form-control" id="viewCountMin" placeholder="0"
          v-model="view_count_min" name="view_count_min">
        </div>
        <div class="form-group col-md-2 col-lg-2">
          <label for="viewCountMax">Maximum View Count</label>
          <input type="number" min=0 class="form-control" id="viewCountMax" placeholder="10000?"
          v-model="view_count_max" name="view_count_max">
        </div>
        <div class="form-group col-md-2 col-lg-2">
          <label for="publishDateMin">Publish date minimum</label>
          <input type="date" class="form-control" id="publishDateMin"
          v-model="date_min" name="date_min">
        </div>
        <div class="form-group col-md-2 col-lg-2">
          <label for="publishDateMax">Publish date maximum</label>
          <input type="date" class="form-control" id="publishDateMax"
          v-model="date_max" name="date_max">
        </div>
        <div class="form-group col-md-4">
          <label for="category">Category</label>
          <select id="category" class="form-control"
          v-model="category" name="category">
            <option v-for="cat in categories" value="cat">{{ cat }}</option>
            <option selected> </option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="reviewed"
          v-model="reviewed" name="reviewed">
          <label class="form-check-label" for="reviewed">
            Reviewed
          </label>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="notReviewed"
          v-model="notReviewed" name="notReviewed">
          <label class="form-check-label" for="notReviewed">
            Not reviewed
          </label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Search</button>
    </form>

    <hr>
    <div class="row">
      <ul>
          <li v-for="journal in queryset">
            <b>{{ journal.title }}| </b>
            <span>Author: {{ journal.author }} | </span>
            <span>Category: </span>
            <span v-for="cat in journal.categories">
                {{ cat }}
            </span>
            <span>| Publish date: {{ journal.publish_date | formatDate }} | </span>
            <span>View count: {{ journal.views }} | </span>
            <span>Reviewed: {{ journal.reviewed }}</span>
          </li>
          <hr>
      </ul>
    </div>
    <div class="spinner-border" role="status" v-if="loading">
      <span class="sr-only">Loading...</span>
    </div>
    <div class="alert alert-danger" v-if="error_msg" role="alert">
      {{ error_msg }}
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
      error_msg: '',

      title_contains: null,
      id_exact: null,
      title_or_author: null,
      view_count_min: null,
      view_count_max: null,
      date_min: null,
      date_max: null,
      category: null,
      reviewed: null,
      notReviewed: null
    }
  },
  filters: {
    formatDate(value){
      return value.split('T')[0]
    }
  },
  methods: {
    onSubmit(){
      let title_contains = this.title_contains
      let id_exact = this.id_exact
      let title_or_author = this.title_or_author
      let view_count_min = this.view_count_min
      let view_count_max = this.view_count_max
      let date_min = this.date_min
      let date_max = this.date_max
      let category = this.category
      let reviewed = this.reviewed
      let notReviewed = this.notReviewed

      this.loading = true
      axios.get('http://127.0.0.1:8000/api/', {
        params: {
          title_contains,
          id_exact,
          title_or_author,
          view_count_min,
          view_count_max,
          date_min,
          date_max,
          category,
          reviewed,
          notReviewed
        }
      })
        .then(response => {
          this.loading = false
          this.queryset = response.data
          this.error_msg = ''
        })
        .catch(error => {
          console.log(error)
          this.loading = false
          this.error_msg = 'Problem połączenia z bazą danych'
        })
    }
  },
  mounted(){
    this.loading = true
    axios.get('http://127.0.0.1:8000/api/')
      .then(response => {
        this.loading = false
        this.queryset = response.data
        this.error_msg = ''
      })
      .catch(error => {
        console.log(error)
        this.loading = false
        this.error_msg = 'Problem połączenia z bazą danych'
      })
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
