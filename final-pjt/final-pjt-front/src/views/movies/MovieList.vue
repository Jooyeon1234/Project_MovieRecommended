<template>
  <div>

    <div class="d-flex justify-content-center mb-5">

      <form @submit.prevent="getMovies" class="d-flex justify-content-center align-items-center">
        <div class="search-bar flex-grow-1">
          <input type="text" v-model.trim="searchMovie" placeholder="검색어를 입력하세요" class="form-control" />
        </div>
        
        <div class="selects">
          <select v-for="filter in filters" :key="filter.name" v-model="$data[filter.name]" class="form-select">
            <option v-for="item in filter.items" v-text="item" :key="item" class="option-list" :value="item"></option>
          </select>
        </div>

        <button class="btn btn-primary">검색</button>
      </form>
    </div>


    <div class="inner">
      <div class="movies">
        <MovieCard v-for="movie in filteredMovies" :key="movie.id" :movie="movie" />
      </div>

      
      <nav aria-label="Page navigation example">
        <ul class="pagination">
          <li class="page-item">
            <button class="page-link arrow-button bg-dark" @click="changePage(1)" :disabled="currentPage === 1">&laquo;</button>
          </li>
          <li class="page-item">
            <button class="page-link arrow-button bg-dark" @click="changePage(currentPage - 1)" :disabled="currentPage === 1">&lt;</button>
          </li>
          <li v-for="page in visiblePages" :key="page" class="page-item">
            <button class="page-link num-page bg-dark" @click="changePage(page)" :class="{ 'current-page': page === currentPage }">{{ page }}</button>
          </li>
          <li class="page-item">
            <button class="page-link arrow-button bg-dark" @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">&gt;</button>
          </li>
          <li class="page-item">
            <button class="page-link arrow-button bg-dark" @click="changePage(totalPages)" :disabled="currentPage === totalPages">&raquo;</button>
          </li>
        </ul>
      </nav>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movie/MovieCard'

export default {
    name: 'MovieView',
    components: {
        MovieCard,
    },
    data(){
        return {
            movies: [],
            filtermovie: '',
            searchMovie: '',
            searchGenre: 'all',
            currentPage: 1,
            moviesPerPage: 20,
            filters: [  
              {
                name: 'searchGenre',
                items: [
                  'all', '액션', '모험', '애니메이션', '코미디', '범죄', '다큐멘터리', 'SF',
                  '드라마', '가족', '판타지', '역사', '공포', '음악', '미스터리', '로맨스',
                  'TV영화', '스릴러', '전쟁', '서부'
                ]
              },
              {
                name: 'moviesPerPage',
                items: [10, 20, 30]
              },
            ],
        }
    },
    watch: {
      moviesPerPage() {
        this.currentPage = 1; // 페이지를 1로 설정
      }
    },
    created() {
        this.getMovies()
    },
    computed: {
      totalPages() {
          return Math.ceil(this.movies.length / this.moviesPerPage)
      },
      filteredMovies() {
        const startIndex = (this.currentPage - 1) * this.moviesPerPage
        const endIndex = startIndex + this.moviesPerPage
        return this.movies.filter(movie =>
          movie.title.toLowerCase().includes(this.filtermovie.toLowerCase())
        ).slice(startIndex, endIndex)
      },
      visiblePages() {
        const totalVisiblePages = 10; // 보여지는 페이지 개수

        // 현재 페이지를 중심으로 앞뒤에 보여질 페이지 수 계산
        const halfVisibleRange = Math.floor((totalVisiblePages - 1) / 2);
        let startPage = Math.max(1, this.currentPage - halfVisibleRange);
        let endPage = Math.min(this.totalPages, startPage + totalVisiblePages - 1);

        // 첫 페이지 기준으로 끝 페이지 조정
        if (endPage === this.totalPages && endPage - startPage + 1 < totalVisiblePages) {
          startPage = Math.max(1, endPage - totalVisiblePages + 1);
        }

        // 끝 페이지 기준으로 시작 페이지 조정
        if (startPage === 1 && endPage - startPage + 1 < totalVisiblePages) {
          endPage = Math.min(this.totalPages, startPage + totalVisiblePages - 1);
        }

        const visiblePages = [];
        for (let i = startPage; i <= endPage; i++) {
          visiblePages.push(i);
        }

        return visiblePages;
      }
    },
    methods: {
        getMovies(){
          if(this.searchMovie === '' && this.searchGenre === 'all'){
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/movies/home/'
            })
                .then((res) => {
                    // console.log(res.data)
                    this.movies = res.data
                    this.currentPage = 1
                })
                .catch((err) => {
                  console.log(err)
                  })
          }else if(this.searchMovie === ''){
            axios({
              method: 'get',
              url: `http://127.0.0.1:8000/movies/search/all/${this.searchGenre}/`
            })
              .then((res) => {
                this.movies = res.data
                this.currentPage = 1
              })
              .catch(err => console.log(err)
              )
          }else{
            axios({
              method: 'get',
              url: `http://127.0.0.1:8000/movies/search/${this.searchMovie}/${this.searchGenre}/`
            })
              .then((res) => {
                this.movies = res.data
                this.currentPage = 1
              })
              .catch(err => console.log(err)
              )
          }

        },
        changePage(page) {
          this.currentPage = page
        },
    }

}
</script>
<style scoped>
    .movies {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      max-width: 1300px;
      margin: 0 auto;
    }
    .container {
    display: flex;
    }
    .container *{
    margin-right: 10px;
    }
    .container .selects {
    display: flex;
    }
    .container .selects .select {
    width: 120px;
    margin-right: 10px;
    }
    .selects{
      display: flex;
  flex-direction: row;
    }
    
    .pagination {
      display: flex;
      justify-content: center;
      margin-top: 20px;
    }

    .pagination button {
      color: #ffffff;
      width: 40px;
      background-color: #3498db;
      border: none;
      outline: none;
      cursor: pointer;
      padding: 8px 12px;
      margin: 0 5px;
      border-radius: 4px;
      transition: background-color 0.3s;
      font-size: 20px;
    }

    .pagination button.current-page {
      background-color: white;
      color: black;
    }

    .pagination button.arrow-button {
      color: white;
      font-weight: bold;
    }

    .pagination button.arrow-button i {
      font-size: 1rem;
    }

    .pagination button:hover {
      background-color: white;
      color: black;
    }


    .option-list {
      color: black;
    }
    input {
      color: black;
    }
</style>