module.exports = {
    purge: [],
    theme: {
        extend: {
            colors: {
                primary: '#041404',
                hover: '#F9CF1C',
                background: '#04340A',
                card: '#017B17',
            },
        },
    },
    variants: {
        extend: {
            position: ['hover', 'focus'],
        },
    },
    plugins: [require('@tailwindcss/forms')],
}
