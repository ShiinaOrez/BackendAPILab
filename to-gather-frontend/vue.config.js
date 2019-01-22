
module.exports = {
    baseUrl: process.env.NODE_ENV === 'production' ? 'https://static.muxixyz.com/to-gather/' : '/', 
    devServer: {
        proxy: {
            '/api/*': {
                target: 'http://localhost:6666/',
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                  '^/api': '/api'
                }
            }
        },
    },
    filenameHashing: false
}
