import { Link, Redirect } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
//import { Button, StyleSheet, Text, TextInput, View } from 'react-native';
import * as React from 'react';
import { View, Text,Button}from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Connexion from './connexion/Connexion';
import Inscription from './connexion/Inscription';
import Test from './test/Test';
import Accueil from './acceuil/Acceuil';



//


const HomeScreen = ({navigation}) => {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('Detail')}
      />
      <Button
          title="Go to connexion"
          onPress={() => navigation.navigate('connexion')}
      />
    </View>
  );
}

const ConnexionScreen = () => {
    return(
        <View>
            <Connexion/>
        </View>
    )
}

const InscriptionScreen = () => {
    return(
        <View>
            <Inscription/>
        </View>
    )
}

const DetailsScreen = () => {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Les details </Text>
    </View>
  );
}

const AccueilScreen = () =>{
  return(
    <View>
        <Accueil/>
    </View>
  )
}

const Stack = createNativeStackNavigator();
//<Redirect href={"/acceuil"}/>
const App = () => {
  return (
    <>

      {/* <Redirect href={"/vente/AjouterVente"}/> */}

        <NavigationContainer independent={true}>
            <Stack.Navigator>
                <Stack.Screen name="Acceuil" component={AccueilScreen} />
                <Stack.Screen name="Home" component={HomeScreen} />
                <Stack.Screen name="Detail" component={DetailsScreen} />
                <Stack.Screen name="Connexion" component={ConnexionScreen} />
                <Stack.Screen name="Inscription" component={InscriptionScreen} />
          </Stack.Navigator>
        </NavigationContainer>
    </>
  );
}

export default App;