import React from 'react';
import Layout from '@theme-original/Layout';
import { useLocation } from '@docusaurus/router';

export default function LayoutWrapper(props) {
  const location = useLocation();
  const isDocs = location.pathname.startsWith('/docs');

  return (
    <Layout
      {...props}
      footer={isDocs ? null : props.footer}
    />
  );
}
