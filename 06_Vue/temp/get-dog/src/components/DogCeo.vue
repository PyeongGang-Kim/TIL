<template>
  <div class="hello">
    <img v-for="image in images" v-bind:key="image.id" v-bind:src="image.url">
    <button v-on:click="getDogImage">개 사진 추가</button>
  </div>
</template>

<script>
export default {

  data: function() {
    return {
      images: [],
    }
  },
  methods: {
    getDogImage = () => {
      axios.get('https://dog.ceo/api/breeds/image/random')
      .then(res => {
        const imgUrl = res.data.message
        this.images.push({
          id: Date.now(),
          url: imgUrl
        })
      })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
