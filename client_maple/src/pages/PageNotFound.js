import React from 'react';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import { Box, Typography } from '@mui/material';
const PageNotFound = () => {

  return (
    <div>
      <NavBar />
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column',
          minHeight: '80vh',
          backgroundColor: 'primary',
        }}
      >
        <Typography variant="h1" >
          404
        </Typography>
        <Typography variant="h6" >
          The page you’re looking for doesn’t exist.
        </Typography>
      </Box>
      <Footer />
    </div>
  );
}

export default PageNotFound;