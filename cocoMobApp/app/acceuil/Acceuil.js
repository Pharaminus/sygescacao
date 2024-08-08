
 import React from 'react';
 import { View, Text, Image, TouchableOpacity, StyleSheet } from 'react-native';
 import { NavigationContainer, useNavigation } from '@react-navigation/native';

const Accueil = () => {
   const navigation = useNavigation();
   return (
     <View>
          <View style={styles.container}>
            <Image
              // source={require('../../assets/images/icon.png')}
              // style={styles.logo}
            />
            <Text style={styles.titre}>Bienvenue !</Text>
            <Text style={styles.texte}>Veuillez sélectionner une option :</Text>
            <TouchableOpacity
              style={styles.bouton}
              onPress={() => navigation.navigate('Connexion')}
      //
            >
              <Text style={styles.boutonTexte}>Se connecter</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={styles.bouton}
              onPress={() => navigation.navigate('Inscription')}
            >
              <Text style={styles.boutonTexte}>S'inscrire</Text>
            </TouchableOpacity>
        </View>
     </View>
   );
 };

 export default Accueil;

 const styles = StyleSheet.create({
   container: {
    //  flex: 1,
     justifyContent: 'center',
     alignItems: 'center',
     backgroundColor: '#f5f5f5',
     height:600,
   },
   logo: {
     width: 100,
     height: 100,
     marginBottom: 20,
   },
   titre: {
     fontSize: 24,
     fontWeight: 'bold',
     marginBottom: 10,
   },
   texte: {
     fontSize: 18,
     marginBottom: 20,
   },
   bouton: {
     backgroundColor: '#4CAF50',
     padding: 10,
     borderRadius: 5,
     marginBottom: 10,
   },
   boutonTexte: {
     color: '#fff',
     fontSize: 18,
   },
 });







