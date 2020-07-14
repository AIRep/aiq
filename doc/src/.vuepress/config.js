module.exports = {
  title: 'An artificial intelligence robot for quantitative trading',
  description: 'Document for aiq',
  locales: {
    '/': {
      lang: 'zh-CN',
    },
  },
  theme: 'meteorlxy',
  themeConfig: {
    lang: 'zh-CN',
    personalInfo: {
      nickname: 'alphaiota',
      description: 'Happy Coding<br/>Happy Life',
      email: 'alphaiota@qq.com',
      location: 'Shanghai, China',
      avatar: '/img/avatar.jpg',
      sns: {
        github: {
          account: 'alphaiota',
          link: 'https://github.com/airep',
        }       
      },
    },
    comments: false,
    header: {
      background: {
        useGeo: true,
      },
      showTitle: true,
    },
    footer: {
      poweredBy: true,
      poweredByTheme: true,
      custom: 'Copyright 2020-present <a href="https://github.com/airep" target="_blank">alphaiota</a> | MIT License',
    },
    infoCard: {
      headerBackground: {
        useGeo: true,
      },
    },
    lastUpdated: true,
    nav: [
      { text: '首页', link: '/', exact: true },
      { text: '文章', link: '/posts/', exact: false },
    ],
    smoothScroll: true,
    zooming: {
      // @see https://vuepress.github.io/en/plugins/zooming
    },
    pagination: {
      perPage: 5,
    },
    defaultPages: {
      home: true,
      posts: true,
    },
  },
}