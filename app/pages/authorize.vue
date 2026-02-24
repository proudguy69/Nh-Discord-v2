<template>
    you are being redirected
</template>

<script setup lang="ts">
import type UserInfo from '~/types/UserInfo'

// interfaces
interface User {
    web_token:string
    username:string
    avatar:string
}

interface AuthResponse {
    success:boolean,
    user:User
}

// varibles
const route = useRoute()
const code = route.query.code

// injects
const appUri = inject('appUri')
const userInfo = inject<Ref<UserInfo>>('userInfo')!


// methods
onMounted(async () => {
    const response = await fetch(`${appUri}/authorize?code=${code}`)
    const data:AuthResponse = await response.json()
    if (!data.success) {return}
    userInfo.value = {
        username: data.user.username!,
        avatar: data.user.avatar!
    }
    localStorage.setItem('web_token', data.user.web_token)
    localStorage.setItem('username', data.user.username)
    localStorage.setItem('avatar', data.user.avatar)
    

})

</script>