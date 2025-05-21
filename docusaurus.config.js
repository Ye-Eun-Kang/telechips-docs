// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'T-Docs',
  tagline: 'Telechips Documentation',
  favicon: 'img/favicon.ico',

  url: 'https://Ye-Eun-Kang.github.io',
  baseUrl: '/telechips-docs/',

  organizationName: 'Ye-Eun-Kang',
  projectName: 'telechips-docs',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // 반드시 require.resolve!
          editUrl: 'https://github.com/Ye-Eun-Kang/telechips-docs/edit/main/',
        },
        theme: {
          
        }
      }),
    ],
  ],

  themeConfig: {
    image: 'img/Telechips_web-icon-192x192.png', // 소셜 공유 썸네일(원하는 이미지로!)
    navbar: {
      title: 'T-Docs',
      logo: {
        alt: 'Telechips Logo',
        src: 'img/Telechips_web-icon-192x192.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'TCC803xSidebar',
          position: 'left',
          label: 'TCC803x',
        },
        {
          type: 'docSidebar',
          sidebarId: 'TCC805xSidebar',
          position: 'left',
          label: 'TCC805x',
        },
        {
          type: 'docSidebar',
          sidebarId: 'TCC807xSidebar',
          position: 'left',
          label: 'TCC807x',
        },
        {
          type: 'docSidebar',
          sidebarId: 'TCC200xSidebar',
          position: 'left',
          label: 'TCC200x',
        },
        {
          type: 'docSidebar',
          sidebarId: 'TCCxxxxSidebar',
          position: 'left',
          label: 'TCCxxxx',
        },
        {
          href: 'https://github.com/Ye-Eun-Kang/telechips-docs',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

module.exports = config;