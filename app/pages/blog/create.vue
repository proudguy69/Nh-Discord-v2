<template>
    <UPageSection>
        <UPageCard variant="subtle">
            <UTextarea v-model="editor_data" class="bg-slate-950"/>
            <UEditor v-model="editor_data" content-type="markdown"></UEditor>
            <UButton @click="submit">Submit</UButton>
        </UPageCard>
    </UPageSection>
</template>

<script setup lang="ts">


const text = ref('# Hello\n\nThis is **markdown**.')

// interface
interface Response {
    success: boolean
}

//varibles
const router = useRouter()

// refs
const editor_data = ref('')

// injects
const appUri = inject('appUri')

// functions
function submit() {
    console.log(editor_data.value)
}

// methods
onMounted(async () => {
    const token = localStorage.getItem('web_token')!
    if (!token) {
        router.push('/')
    }
    const response = await fetch(`${appUri}/permission`, {headers:{'Authorize':token}})
    const data:Response = await response.json()
    if (!data.success) {
        router.push('/')
    }

})

</script>