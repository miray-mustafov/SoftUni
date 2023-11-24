function construction_crew(worker_obj){
    if(worker_obj.dizziness === false){
        return worker_obj
    }

    worker_obj.dizziness = false
    worker_obj.levelOfHydrated += worker_obj.weight * worker_obj.experience * 0.1
    return worker_obj
}


  console.log(construction_crew({ 
    weight: 80,
    experience: 1,
    levelOfHydrated: 0,
    dizziness: true 
}
  ))
  console.log(construction_crew({ weight: 120,
    experience: 20,
    levelOfHydrated: 200,
    dizziness: true }
  ))