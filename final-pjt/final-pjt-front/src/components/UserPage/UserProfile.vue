<template>
    <div class="profile">
        <div>
            <!-- <img :src="userImg" alt="profile img"> -->
        </div>
        <div>
            <h1>{{ userprofile.nickname }}</h1>
            <p>팔로워 수: {{ followersCount }}</p>
            <p>팔로잉 수: {{ userprofile.followings_count }}</p>
            <button v-if="!isCurrentUser" @click="toggleFollow">
                {{ isFollowing ? '언팔로우' : '팔로우' }}
            </button>
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
            followersCount : 0
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

        console.log(this.isCurrentUser)

        if (this.userprofile.followers.includes(this.userInfo.pk)){
            this.isFollowing = true
        }
    },
    computed:{
        ...mapGetters(['userprofile', 'userInfo']),
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

<style>

</style>