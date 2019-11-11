<template>
  <div>
    <search-bar @myInputChange="onInputChange"></search-bar>
    <video-list :videos="videos"></video-list>
  </div>
</template>

<script>
import axios from "axios"
import SearchBar from "./components/SearchBar"
import VideoList from "./components/VideoList"

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'app',
  data(){
    return {videos: [],
    }
  },
  components: {
    SearchBar, VideoList
  },
  methods: {
    onInputChange(inputValue){
      axios.get(API_URL, {
        params: {
          // 1. 위에서 가져 온 키
          key: API_KEY,
          // 2. (옵션) 특정 리소스 유형만 검색(channel, playlist, video 등)
          type: 'video',
          // 3. (required) API 응답이 포함하는 search 리소스 속성
          part: 'snippet',
          // 4. (option) string -> 검색어(사용자에게 받은 input value)
          q: inputValue,
        }
      })
      .then(response => {
        // console.log(response)
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>


</style>
