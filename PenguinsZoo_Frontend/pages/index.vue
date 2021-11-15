<template class="h-full">
    <div class="relative h-full">
        <Navbar></Navbar>
        <div class="lg:pb-5 h-64 lg:h-full">
            <HomeDetail></HomeDetail>
        </div>
        <HomeDetail2></HomeDetail2>
        <Footer></Footer>
    </div>
</template>

<script>
import Navbar from '~/components/layouts/NavBar'
import Footer from '~/components/layouts/Footer'
import HomeDetail from '~/components/HomeDetail'
import HomeDetail2 from '~/components/HomeDetail2'
export default {
    components: { HomeDetail2, HomeDetail, Footer, Navbar },
    data() {
        return {
            title: 'Penguins Vietnam',
            infinite_key: '',
        }
    },
    head() {
        return {
            title: this.title,
            meta: [
                { hid: 'og-title', property: 'og:title', content: this.title },
            ],
        }
    },
}
</script>

<style>
html {
    height: 100%;
}

body {
    height: 100%;
}

div#__nuxt {
    height: 100%;
}

div#__layout {
    height: 100%;
}
</style>
