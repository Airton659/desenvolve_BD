package com.example.model;

import java.lang.annotation.Inherited;

import javax.persistence.*;
import org.hibernate.annotations.Type;

@Entity
public class Partner {
    
    @Id
    private String id;

    private String trandingName;
    private String ownerName;

    @Column(unique = true)
    private String document;

    @Type(type="json")
    @Column(columnDefinition = "json")
    private String coverageArea;

    @Type(type="json")
    @Column(columnDefinition = "json")
    private String addres;


}