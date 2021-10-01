module.exports = {
    devServer: {
        // proxy: {
        //     '^/api': {
        //         target: "http://localhost:8000",
        //         changeOrigin: true
        //     },
        // }
    },
    lintOnSave: false,
    runtimeCompiler: true,
    configureWebpack: {
        //Necessary to run npm link https://webpack.js.org/configuration/resolve/#resolve-symlinks
        resolve: {
            symlinks: false
        }
    },
    transpileDependencies: [
        '@coreui/utils',
        '@coreui/vue'
    ]
}