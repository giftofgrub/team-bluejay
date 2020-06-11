import React from "react";
import { MuiThemeProvider } from "@material-ui/core";
import { theme } from "themes/theme";

import { Provider as AuthProvider } from "contexts/AuthContext";
import { Provider as MealProvider } from "contexts/MealContext";
import { Provider as AlertProvider } from "contexts/AlertContext";
import { DialogProvider } from "contexts/DialogContext";
import { CuisineProvider } from "contexts/CuisineContext";

const RootProvider = ({ children }) => {
  return (
    <MuiThemeProvider theme={theme}>
      <AlertProvider>
        <AuthProvider>
          <MealProvider>
            <CuisineProvider>
              {/* DialogProvider must be the innermost provider so that its children can use contexts from outermost parent providers */}
              <DialogProvider>{children}</DialogProvider>
            </CuisineProvider>
          </MealProvider>
        </AuthProvider>
      </AlertProvider>
    </MuiThemeProvider>
  );
};

export default RootProvider;
