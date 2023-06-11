<template>
  <div class="container">
    <h1 class="animate-slide-from-right">
        <span>TMTV API</span><br>
        THE OPEN<br>
        MOVIE DATABASE
    </h1>
    <h3 class="animate-slide-from-bottom">This is a movie site made using DRF and Vue.js.</h3>
  </div>
</template>

<script>
export default {
    name: 'HeadLine',
    mounted() {
      this.animateHeadline();
    },
    methods: {
      animateHeadline() {
        const h1 = document.querySelector('.animate-slide-from-right');
        const h3 = document.querySelector('.animate-slide-from-bottom');
        
        h1.style.opacity = '0';
        h1.style.transform = 'translateX(100px)';
        h1.style.transition = 'opacity 0.8s ease-in, transform 1s ease-in-out';
        setTimeout(() => {
          h1.style.opacity = '1';
          h1.style.transform = 'translateX(0)';
        }, 300);
        
        h3.style.opacity = '0';
        h3.style.transform = 'translateY(50px)';
        h3.style.transition = 'opacity 0.8s ease-in, transform 1s ease-in-out';
        setTimeout(() => {
          h3.style.opacity = '1';
          h3.style.transform = 'translateY(0)';
        }, 600);
      }
    }
}
</script>

<style scoped>
.container {
  padding-top: 40px;
  display: flex;
  flex-direction: column;
  border: solid 5px white;
}

h1 {
  line-height: 1;
  font-family: "Oswald", sans-serif;
  font-size: 80px;
}

h1 span {
  color: blue;
}

h3 {
  margin-top: 30px;
  color: white;
}

.animate-slide-from-right {
  opacity: 0;
  transform: translateX(100px);
}

.animate-slide-from-bottom {
  opacity: 0;
  transform: translateY(50px);
}
</style>
