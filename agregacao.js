// Pipeline de Agregação para ser executado na collection 'Carros'
// colado diretamente no shell do MongoDB 

db.getCollection('Carros').aggregate([
    {
      $lookup: {
        from: 'Montadoras',          
        localField: 'Montadora',     
        foreignField: 'Montadora',    
        as: 'dados_da_montadora'     
      }
    },
    {
      $unwind: {
        path: '$dados_da_montadora'
      }
    },
    {

      $group: {
        _id: '$dados_da_montadora.Pais', 
        Carros: {
          $push: {
            Carro: '$Carro',
            Cor: '$Cor',
            Montadora: '$Montadora'
          }
        }
      }
    },
    {
      $project: {
        _id: 0,
        Pais: '$_id', 
        Carros: '$Carros' 
      }
    },
    {
        $sort: {
            Pais: 1
        }
    }
  ]);