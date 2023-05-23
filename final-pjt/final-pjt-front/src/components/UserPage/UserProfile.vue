<template>
    <div class="profile">
        <div>
            <!-- <img :src="userImg" alt="profile img"> -->
        </div>
        <div>
            <h1>{{ nickname }}</h1>
            <p>팔로워 수: {{ userprofile.followersCount }}</p>
            <p>팔로잉 수: {{ userprofile.followingsCount }}</p>
            <button v-if="!isCurrentUser" @click="toggleFollow">
                {{ isFollowing ? '언팔로우' : '팔로우' }}
            </button>
        </div>  
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name:'UserProfile',
    data() {
        return {
        userinfo : this.$store.state.user,
        nickname: this.userprofile.nickname,            // 사용자 이름
        followersCount: this.userprofile.followers_count,       // 팔로워 수
        followingsCount: this.userprofile.followings_count,      // 팔로잉 수
        isFollowing: false       // 현재 사용자가 팔로우 중인지 여부
        };
    },
    computed:{
        ...mapGetters(['userprofile'])
    }
}
</script>

<style>

</style>