module.exports = function(grunt) {
    grunt.initConfig({
        // running `grunt less` will compile once
        less: {
            development: {
                options: {
                    paths: ["./css"],
                    yuicompress: true
                },
                files: {
                    "./css/base.css": "./css/base.less"
                }
            }
        },
        // running `grunt watch` will watch for changes
        watch: {
            files: ["./css/*.less", "./css/*/*.less"],
            tasks: ["less"]
        }
    });
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
};
