<template>
    
</template>

<script setup lang="ts">
import type UserInfo from '~/types/UserInfo';

// varibles
const router = useRouter()

// injects
const userInfo = inject<Ref<UserInfo>>('userInfo')!
const appUri = inject('appUri')

// methods
onMounted(async () => {
    userInfo.value = {
        username: undefined,
        avatar: undefined
    }
    const token = localStorage.getItem('web_token')!

    console.log(token)

    const response = await fetch(`${appUri}/logout`, {
        method: 'GET',
        headers: {'Authorize': token}
    })

    localStorage.removeItem('web_token')
    localStorage.removeItem('avatar')
    localStorage.removeItem('username')

    router.push('/')
})

</script>