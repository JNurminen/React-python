describe('Contacts sovellus', function () {

  beforeEach(function () {
      cy.visit('http://localhost:5173')
  })
   // Testaa että sivu avautuu ja näyttää datarivejä
  it('Sivu avautuu ja näyttää datarivejä', function () {
      cy.visit('http://localhost:5173') // avaa sivun 
      cy.contains('Name') // jos on saatu dataa kannasta
      cy.contains('Role') // jos on saatu dataa kannasta
      cy.contains('Job Description') // jos on saatu dataa kannasta
      cy.contains('Gender') // jos on saatu dataa kannasta
  })

  // Testaa että uuden ystävän lisääminen onnistuu
  it('should add a new Friend', () => {
    cy.contains('Create Friend').click(); // painaa nappia "Create Friend"
    
    // Täytä lomake ja lähetä se
    cy.get('#name').type('Alice'); 
    cy.get('#role').type('admin'); 
    cy.get('#description').type('Alice is an admin'); 
    cy.get('#gender').type('female'); 

    cy.get('[data-testid="submit-button"]').should('be.visible').click(); // painaa nappia "Create"
    
    // Tarkista että uusi ystävä on lisätty
    cy.contains('Name:');
    cy.contains('Role:');
    cy.contains('Job Description:');
    cy.contains('Gender');
  });
});