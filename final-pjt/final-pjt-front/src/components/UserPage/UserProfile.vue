<template>
    <div class="profile">
    <div>
      <img :src="`http://127.0.0.1:8000${userImg}`" alt="profile img" style="border-radius: 50%; margin-top: 30px; ">
      <br><br>
      <h1>{{ userprofile.nickname }}</h1>
      <v-btn
      elevation="2" color="#7c5091"
      style="color:white; width:200px; font-weight: bold; margin-bottom: 20px;"
      v-if="!isCurrentUser" @click="toggleFollow">
        {{ isFollowing ? '언팔로우' : '팔로우' }}
      </v-btn>
    </div>
    <div class="user-info">
      <div class="information"><i class="fa-solid fa-film fa-2xl icon" style="color: #7c5091;"></i><span>{{ likeMovie }}</span><p>영화</p></div>
      <div class="horizion"></div>
      <div class="information"><i class="fa-solid fa-comments fa-2xl icon" style="color: #7c5091;"></i><span>{{ comment }}</span><p>리뷰</p></div>
      <div class="horizion"></div>
      <div class="information"><i class="fa-solid fa-user-group fa-2xl icon" style="color: #7c5091;"></i><span>{{ followersCount }}</span><p>팔로워</p></div>
      <div class="horizion"></div>
      <div class="information"><i class="fa-solid fa-user-plus fa-2xl icon" style="color: #7c5091;"></i><span>{{  userprofile.followings_count }}</span><p>팔로잉</p></div>
    </div>  
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'UserProfile',
    data() {
        return {
            isCurrentUser : false,  
            isFollowing : false,
            followersCount : 0,
            likeMovie:0,
            comment:0
        };
    },
    created(){
        this.getUserProfile()

        this.followersCount = this.userprofile.followers_count

        if (this.userprofile.pk != this.userInfo.pk){
            this.isCurrentUser = false
        }else{
            this.isCurrentUser = true
        }

        // console.log(this.isCurrentUser)

        if (this.userprofile.followers.includes(this.userInfo.pk)){
            this.isFollowing = true
        }

        this.likeMovie = (this.userprofile.like_now_playing_movies.length
            + this.userprofile.like_upcoming_movies.length + this.userprofile.like_popular_movies.length)
        
            this.comment = (this.userprofile.nowplayingreview_set.length
            + this.userprofile.upcomingreview_set.length + this.userprofile.popularreview_set.length) 
    },
    computed:{
        ...mapGetters(['userprofile', 'userInfo']),
        userImg(){
            if (!this.userprofile.user_image){
                return '/media/profile_images/user_img.png'
            }
            return this.userprofile.user_image
        }
    },
    methods:{
        getUserProfile(){
            const userId = this.$route.params.userid
            this.$store.dispatch('getUserProfile', userId)
        },
        toggleFollow() {
            // 팔로우/언팔로우 버튼 클릭 시 실행되는 함수
            if (this.isFollowing) {
                this.unfollowUser();
            } else {
                this.followUser();
            }
        },
        followUser() {
        // 팔로우 API 요청
            const token = this.$store.state.login.token
            const from_user_id = this.userInfo.pk
            const to_user_id = this.userprofile.pk
            
            axios({
                method:'post',
                url : `${API_URL}/accounts/follow/${this.userprofile.pk}/`,
                data : {
                    from_user_id, to_user_id
                },
                headers:{
                    Authorization : `Token ${token}`
                }
            })
            .then((res)=>{
                console.log(res)
                console.log('follow success')
                this.isFollowing = true;
                this.followersCount++;
                this.$store.commit('ADD_FOLLOW', from_user_id)
            })
            .catch(()=>{
                console.log('follow fail')
            })
        },
        unfollowUser() {
        // 팔로우 API 요청
            const token = this.$store.state.login.token
            const from_user_id = this.userInfo.pk
            const to_user_id = this.userprofile.pk

            axios({
                method:'post',
                url : `${API_URL}/accounts/follow/${this.userprofile.pk}/`,
                data : {
                    from_user_id, to_user_id
                },
                headers:{
                    Authorization : `Token ${token}`
                }
            })
            .then(()=>{
                console.log('unfollow success')
                this.isFollowing = false;
                this.followersCount--;
                this.$store.commit('DELETE_FOLLOW', from_user_id)
            })
            .catch(()=>{
                console.log('unfollow fail')
            })
        },
}
}
</script>

<style scoped>
.profile{
  background: linear-gradient( rgb(0, 0, 0), #513581, rgb(0, 0, 0));
  box-shadow:-2 1 5px #7E57C2;
  margin: auto;
  margin-top: 10px;
  border-radius: 10px;
  color: white;
}
img {
  width: 300px;
  height: 300px;
}
.user-info{
  display: flex;
  justify-content: space-evenly;
}
.information{
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-content: stretch;
}
.horizion{
  width: 2px;
  height: 130px;
  background-color: #2f2148;
  box-shadow:0 0 8px #7E57C2;
  margin-top: 10px;
}.icon{
  margin-bottom: 17px;
}
</style>